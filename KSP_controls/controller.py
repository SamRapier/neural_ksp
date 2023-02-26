import time

class FlightController:
    def __init__(self, curr_vessel):
        self.vessel_controller = curr_vessel.control
        self.throttle = self.vessel_controller.throttle
        self.yaw = self.vessel_controller.yaw
        self.roll = self.vessel_controller.roll
        self.pitch = self.vessel_controller.pitch

    def get_control_positions(self):
        return (self.throttle, self.yaw, self.roll, self.pitch)

    # Throttle Controls
    def set_throttle(self, value:float):
        try:
            if value < 0 or value > 1:
                raise ValueOutOfBoundsException
            try:
                self.throttle = value
                self.vessel_controller.throttle = self.throttle
            except:
                print("Error setting throttle")
            
        except TypeError:
            print("Throttle value must be a float")
        except ValueOutOfBoundsException:
            print("Throttle value must be between 0 and 1")
        except:
            print("Unexpected error when setting throttle value")
        finally:
            return self.throttle

        
    def adjust_throttle(self, value:float):
        try:
            if value < -1 or value > 1:
                raise ValueOutOfBoundsException

            try:
                self.throttle += value
                if self.throttle < 0:
                    self.throttle = 0
                elif self.throttle > 1:
                    self.throttle = 1
                
                self.vessel_controller.throttle = self.throttle

            except:
                print("Error adjusting throttle")

        except TypeError:
            print("Throttle value must be a float")
        except ValueOutOfBoundsException:
            print("Throttle adjustment value must be between -1 and 1")
        except:
            print("Unexpected error when adjusting throttle value")
        finally:
            return self.throttle
        
        
    # Yaw controls
    def set_yaw(self, value:float):
        try: 
            if value < -1 or value > 1:
                raise ValueOutOfBoundsException
        
            try:
                self.yaw = value
                self.vessel_controller.yaw = self.yaw
            except:
                print("Error setting yaw")
            
        except TypeError:
            print("Yaw value must be a float")
        except ValueOutOfBoundsException:
            print("Yaw value must be between -1 and 1")
        except:
            print("Unexpected error when setting yaw value")
        finally:
            return self.yaw
        
    def adjust_yaw(self, value:float):
        try:
            if value < -2 or value > 2:
                raise ValueOutOfBoundsException
        
            try:
                self.yaw += value
                if self.yaw < -1:
                    self.yaw = -1
                elif self.yaw > 1:
                    self.yaw = 1
                
                self.vessel_controller.yaw = self.yaw

            except:
                print("Error adjusting yaw")
        
        except TypeError:
            print("Yaw value must be a float")
        except ValueOutOfBoundsException:
            print("Yaw adjustment value must be between -2 and 2")
        except:
            print("Unexpected error when adjusting yaw value")
        finally:
            return self.yaw
        
    # Roll controls
    def set_roll(self, value:float):
        try:       
            if value < -1 or value > 1:
                raise ValueOutOfBoundsException
        
            try:
                self.roll = value
                self.vessel_controller.roll = self.roll

            except:
                print("Error setting roll")
            
        except TypeError:
            print("Roll value must be a float")
        except ValueOutOfBoundsException:
            print("Roll value must be between -1 and 1")
        except:
            print("Unexpected error when setting roll value")
        finally:
            return self.roll
        
    def adjust_roll(self, value:float):
        try:
            if value < -2 or value > 2:
                raise ValueOutOfBoundsException
        
            try:
                self.roll += value
                if self.roll < -1:
                    self.roll = -1
                elif self.roll > 1:
                    self.roll = 1
                
                self.vessel_controller.roll = self.roll

            except:
                print("Error adjusting roll")

        except TypeError:
            print("Roll value must be a float")
        except ValueOutOfBoundsException:
            print("Roll adjustment value must be between -2 and 2")
        except:
            print("Unexpected error when adjusting roll value")
        finally:
            return self.roll
        
    # Pitch controls
    def set_pitch(self, value:float):
        try:
            if value < -1 or value > 1:
                raise ValueOutOfBoundsException
        
            try:
                self.pitch = value
                self.vessel_controller.pitch = self.pitch
                
            except:
                print("Error setting pitch")

        except TypeError:
            print("Pitch value must be a float")
        except ValueOutOfBoundsException:
            print("Pitch value must be between -1 and 1")
        except:
            print("Unexpected error when setting pitch value")
        finally:
            return self.pitch
        
    def adjust_pitch(self, value:float):
        try:
            if value < -2 or value > 2:
                raise ValueOutOfBoundsException
        
            try:
                self.pitch += value
                if self.pitch < -1:
                    self.pitch = -1
                elif self.pitch > 1:
                    self.pitch = 1
                
                self.vessel_controller.pitch = self.pitch
                
            except:
                print("Error adjusting pitch")

        except TypeError:
            print("Pitch value must be a float")
        except ValueOutOfBoundsException:
            print("Pitch adjustment value must be between -2 and 2")
        except:
            print("Unexpected error when adjusting pitch value")
        finally:
            return self.pitch

    def deploy_parachutes(self):
        self.vessel_controller.parachutes = True

    def set_sas(self, sas_enabled):
        self.vessel_controller.sas = sas_enabled
    
    def get_nav_ball_speed(self):
        return self.vessel_controller.speed_mode


class StagingController:
    def __init__(self, curr_vessel):
        try:
            self.vessel_controller = curr_vessel.control
            self.vessel_parts = curr_vessel.parts
            self.curr_stage = 0

        except:
            print("Vessel cannot be assigned")

    def activate_next_stage(self):
        self.vessel_controller.activate_next_stage()
        self.curr_stage = self.vessel_controller.current_stage

    def get_current_stage(self):
        self.curr_stage = self.vessel_controller.current_stage
        return self.curr_stage

    def get_parts_to_be_decoupled(self):
        in_decouple_stage_parts = self.vessel_parts.in_decouple_stage(self.get_current_stage() -1)
        return in_decouple_stage_parts

    def get_engines_to_be_decoupled(self):
        decouple_stage_parts = self.get_parts_to_be_decoupled()
        engines_to_be_decoupled = []

        for part in decouple_stage_parts:
            if part.engine:
                engines_to_be_decoupled.append(part.engine)
        
        return engines_to_be_decoupled
    
    def unstage_parts_when_fuel_empty(self):
        engines_to_be_decoupled = self.get_engines_to_be_decoupled()
        engines_have_fuel = True

        while engines_have_fuel:
            for engine in engines_to_be_decoupled:
                if engine.has_fuel:
                    engines_have_fuel = True
                    break
                else:
                    print("Engines empty")
                    engines_have_fuel = False
                    # should only reach here if no engines have fuel
            
        # sleep for 3 seconds then decouple
        time.sleep(1)
        print("decoupling...")       
        self.activate_next_stage()



            



class ValueOutOfBoundsException(Exception):
    "Raised when the input value is out of bounds"
    pass