#pragma once
// clang-format off

#define MACHINE_NAME            "6 Pack 2130 XYZ Mosfets"

#define N_AXIS 3

// I2S (steppers & other output-only pins)
#define USE_I2S_OUT
#define USE_I2S_STEPS
//#define DEFAULT_STEPPER ST_I2S_STATIC

#define I2S_OUT_BCK      GPIO_NUM_22
#define I2S_OUT_WS       GPIO_NUM_17
#define I2S_OUT_DATA     GPIO_NUM_21

#define TRINAMIC_RUN_MODE           Motors::TrinamicMode::CoolStep
// #define TRINAMIC_HOMING_MODE        Motors::TrinamicMode::StallGuard

// Motor Socket #1
#define X_TRINAMIC_DRIVER       2130
#define X_DISABLE_PIN           I2SO(0)
#define X_DIRECTION_PIN         I2SO(1)
#define X_STEP_PIN              I2SO(2)
#define X_CS_PIN                I2SO(3)
#define X_RSENSE                TMC2130_RSENSE_DEFAULT

// Motor Socket #2
#define Y_TRINAMIC_DRIVER       X_TRINAMIC_DRIVER
#define Y_DIRECTION_PIN         I2SO(4)
#define Y_STEP_PIN              I2SO(5)
#define Y_DISABLE_PIN           I2SO(7)
#define Y_CS_PIN                I2SO(6)
#define Y_RSENSE                X_RSENSE

// Motor Socket #3
#define Z_TRINAMIC_DRIVER       X_TRINAMIC_DRIVER
#define Z_DISABLE_PIN           I2SO(8)
#define Z_DIRECTION_PIN         I2SO(9)
#define Z_STEP_PIN              I2SO(10)
#define Z_CS_PIN                I2SO(11)
#define Z_RSENSE                X_RSENSE


/*
    Socket I/O reference
    The list of modules is here...
    https://github.com/bdring/6-Pack_CNC_Controller/wiki/CNC-I-O-Module-List
    Click on each module to get example for using the modules in the sockets

Socket #1
#1 GPIO_NUM_33 (Sg1)
#2 GPIO_NUM_32 (Sg2)
#3 GPIO_NUM_35 (Sg3) (input only)
#4 GPIO_NUM_34 (Sg4) (input only)

Socket #2
#1 GPIO_NUM_2
#2 GPIO_NUM_25
#3 GPIO_NUM_39 (Sg5) (input only)
#4 GPIO_NUM_36 (Sg6) (input only)

Socket #3
#1 GPIO_NUM_26
#2 GPIO_NUM_4
#3 GPIO_NUM_16
#4 GPIO_NUM_27

Socket #4
#1 GPIO_NUM_14
#2 GPIO_NUM_13
#3 GPIO_NUM_15
#4 GPIO_NUM_12

Socket #5
#1 I2SO(24)  (output only)
#2 I2SO(25)  (output only)
#3 I2SO26)  (output only)

*/


// Socket #1 (Empty)
// Install StallGuard Jumpers
// #define Z_LIMIT_PIN             GPIO_NUM_35  // Sg3

// Socket #2 4x Input Module
// https://github.com/bdring/6-Pack_CNC_Controller/wiki/4x-Switch-Input-module
#define X_LIMIT_PIN             GPIO_NUM_2
#define Y_LIMIT_PIN             GPIO_NUM_25
#define Z_LIMIT_PIN             GPIO_NUM_39





// Example Quad MOSFET module in socket #3
// https://github.com/bdring/6-Pack_CNC_Controller/wiki/Quad-MOSFET-Module
#define COOLANT_MIST_PIN       GPIO_NUM_26  // M7
#define COOLANT_FLOOD_PIN      GPIO_NUM_4   // M8
#define USER_DIGITAL_PIN_0     GPIO_NUM_16  // M62 P0 and M63P0
#define USER_ANALOG_PIN_0      GPIO_NUM_27  // M67 E0 Q23.87 (set set output#1 to 23.87% duty)

// === Default settings
#define DEFAULT_STEP_PULSE_MICROSECONDS I2S_OUT_USEC_PER_PULSE

#define DEFAULT_INVERT_LIMIT_PINS       1

#define INVERT_LIMIT_PIN_MASK BIT(Z_AXIS) // invert Y
