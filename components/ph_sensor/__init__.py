import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import (
    CONF_ID, CONF_ADDRESS, 
    DEVICE_CLASS_PH, STATE_CLASS_MEASUREMENT, UNIT_PH,
    ICON_GAUGE
)
from esphome import automation

DEPENDENCIES = ['i2c']
AUTO_LOAD = ['sensor']

ph_sensor_ns = cg.esphome_ns.namespace('ph_sensor')
PH_Sensor = ph_sensor_ns.class_('PH_Sensor', cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = sensor.sensor_schema(
    PH_Sensor,
    unit_of_measurement=UNIT_PH,
    icon=ICON_GAUGE,
    accuracy_decimals=2,
    device_class=DEVICE_CLASS_PH,
    state_class=STATE_CLASS_MEASUREMENT,
).extend({
    cv.GenerateID(): cv.declare_id(PH_Sensor),
    cv.Optional(CONF_ADDRESS, default=0x00): cv.i2c_address,
}).extend(cv.polling_component_schema('60s'))


async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    
    if CONF_ADDRESS in config and config[CONF_ADDRESS] != 0x00:
        cg.add(var.set_address(config[CONF_ADDRESS]))