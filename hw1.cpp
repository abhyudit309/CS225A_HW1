#include "Sai2Model.h"
#include "redis/RedisClient.h"
#include "timer/LoopTimer.h"

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

#define QUESTION_1   1
#define QUESTION_2   2
#define QUESTION_3   3
#define QUESTION_4   4
#define QUESTION_5   5
#define QUESTION_6   6

// handle ctrl-c nicely
#include <signal.h>
bool runloop = true;
void sighandler(int sig)
{ runloop = false; }

using namespace std;
using namespace Eigen;

const string robot_file = "./resources/panda_arm_controller.urdf";
const string robot_name = "PANDA";

// redis keys:
// - read:
const std::string JOINT_ANGLES_KEY = "sai2::cs225a::panda_robot::sensors::q";
const std::string JOINT_VELOCITIES_KEY = "sai2::cs225a::panda_robot::sensors::dq";
// - write
const std::string JOINT_TORQUES_COMMANDED_KEY = "sai2::cs225a::panda_robot::actuators::fgc";
const string CONTROLLER_RUNING_KEY = "sai2::cs225a::controller_running";

unsigned long long controller_counter = 0;

int main() {

	// start redis client
	auto redis_client = RedisClient();
	redis_client.connect();

	// set up signal handler
	signal(SIGABRT, &sighandler);
	signal(SIGTERM, &sighandler);
	signal(SIGINT, &sighandler);

	// load robots
	auto robot = new Sai2Model::Sai2Model(robot_file, false);
	robot->_q = redis_client.getEigenMatrixJSON(JOINT_ANGLES_KEY);
	VectorXd initial_q = robot->_q;
	robot->updateModel();

	// prepare controller
	int dof = robot->dof();
	VectorXd command_torques = VectorXd::Zero(dof);

	// **********
	// code added
	VectorXd q_desired(dof);
	q_desired << 90.0, -45.0, 0.0, -125.0, 0.0, 80.0, 0.0; // in degrees
	q_desired *= M_PI/180.0;
	VectorXd gravity = VectorXd::Zero(dof);
	VectorXd coriolis_term = VectorXd::Zero(dof);
	double m11 = robot->_M(0,0);
	ofstream file;
	file.open("../../hw1/data_files/q6.txt"); // change this according to the question

	// extra credit
	double mass_payload = 2.5;
	std::string ee_link_name = "link7";
	Vector3d ee_pos_in_link = Vector3d(0.0, 0.0, 0.17);
	MatrixXd ee_jacobian(3, dof);
	Vector3d g = Vector3d(0.0, 0.0, -9.81);
	// **********

	// create a timer
	LoopTimer timer;
	timer.initializeTimer();
	timer.setLoopFrequency(1000); 
	double start_time = timer.elapsedTime(); //secs
	bool fTimerDidSleep = true;

	redis_client.set(CONTROLLER_RUNING_KEY, "1");
	while (runloop) {
		// wait for next scheduled loop
		timer.waitForNextLoop();
		double time = timer.elapsedTime() - start_time;

		// read robot state from redis
		robot->_q = redis_client.getEigenMatrixJSON(JOINT_ANGLES_KEY);
		robot->_dq = redis_client.getEigenMatrixJSON(JOINT_VELOCITIES_KEY);
		robot->updateModel();

		// **********************
		// WRITE YOUR CODE AFTER
		// **********************
		int controller_number = QUESTION_6;  // change to the controller of the question you want : QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5, QUESTION_6

		// ---------------------------  question 1 ---------------------------------------
		if(controller_number == QUESTION_1)
		{
			double kp = 400.0;                // chose your p gain
			double kv = 2 * sqrt(m11 * kp);   // chose your d gain
			
			command_torques = -kp * (robot->_q - q_desired) - kv * robot->_dq;
		}

		// ---------------------------  question 2 ---------------------------------------
		if(controller_number == QUESTION_2)
		{
			double kp = 400.0;                // chose your p gain
			double kv = 2 * sqrt(m11 * kp);   // chose your d gain

			robot->gravityVector(gravity);
			command_torques = -kp * (robot->_q - q_desired) - kv * robot->_dq + gravity;
		}

		// ---------------------------  question 3 ---------------------------------------
		if(controller_number == QUESTION_3)
		{
			double kp = 400.0;      // chose your p gain
			double kv = 40.0;       // chose your d gain

			robot->gravityVector(gravity);
			command_torques = robot->_M * (-kp * (robot->_q - q_desired) - kv * robot->_dq) + gravity;
		}

		// ---------------------------  question 4 ---------------------------------------
		if(controller_number == QUESTION_4)
		{
			double kp = 400.0;      // chose your p gain
			double kv = 40.0;       // chose your d gain

			robot->gravityVector(gravity);
			robot->coriolisForce(coriolis_term);
			command_torques = robot->_M * (-kp * (robot->_q - q_desired) - kv * robot->_dq) + coriolis_term + gravity;
		}

		// ---------------------------  question 5 ---------------------------------------
		if(controller_number == QUESTION_5)
		{
			double kp = 400.0;      // chose your p gain
			double kv = 40.0;       // chose your d gain

			robot->gravityVector(gravity);
			robot->coriolisForce(coriolis_term);
			command_torques = robot->_M * (-kp * (robot->_q - q_desired) - kv * robot->_dq) + coriolis_term + gravity;
		}

		// ---------------------------  question 6 (extra credit) -------------------------
		if(controller_number == QUESTION_6)
		{
			double kp = 400.0;      // chose your p gain
			double kv = 40.0;       // chose your d gain

			robot->Jv(ee_jacobian, ee_link_name, ee_pos_in_link);
			auto mass_correction = mass_payload * ee_jacobian.transpose() * ee_jacobian;
			auto gravity_correction = -mass_payload * ee_jacobian.transpose() * g;
			
			robot->gravityVector(gravity);
			robot->coriolisForce(coriolis_term);
			command_torques = (robot->_M + mass_correction) * (-kp * (robot->_q - q_desired) - kv * robot->_dq) + coriolis_term + gravity + gravity_correction;
		}

		// writing trajectory to txt file
		auto error = robot->_q - q_desired;
		if (error.norm() >= 0.05) {
			file << robot->_q.transpose() << "\t" << robot->_dq.transpose() << "\n";
		} else {
			file.close();
		}

		// **********************
		// WRITE YOUR CODE BEFORE
		// **********************

		// send to redis
		redis_client.setEigenMatrixJSON(JOINT_TORQUES_COMMANDED_KEY, command_torques);

		controller_counter++;

	}

	command_torques.setZero();
	redis_client.setEigenMatrixJSON(JOINT_TORQUES_COMMANDED_KEY, command_torques);
	redis_client.set(CONTROLLER_RUNING_KEY, "0");

	double end_time = timer.elapsedTime();
    std::cout << "\n";
    std::cout << "Controller Loop run time  : " << end_time << " seconds\n";
    std::cout << "Controller Loop updates   : " << timer.elapsedCycles() << "\n";
    std::cout << "Controller Loop frequency : " << timer.elapsedCycles()/end_time << "Hz\n";

	return 0;
}
