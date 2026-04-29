#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/i2c/i2c_device.h"
#include "iarduino_I2C_pH.h"

namespace esphome {
namespace ph_sensor {

class PH_Sensor : public sensor::Sensor, public PollingComponent, public i2c::I2CDevice {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;
  
  void set_address(uint8_t address) { this->address_ = address; }

 protected:
  iarduino_I2C_pH ph_;
  uint8_t address_ = 0x00;
};

}  // namespace ph_sensor
}  // namespace esphome