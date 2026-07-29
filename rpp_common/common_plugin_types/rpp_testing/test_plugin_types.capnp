@0xbadbadbadbadbbd1;
using Msgs = import "rpp_common/msgs.capnp";
using Anot = import "rpp_common/anot.capnp";

interface Controller(State, Command) {
  step     @0 (state :State, dt :Float64) -> (command :Command);
  validate @1 (state :State) -> (ok :Bool);
}


interface DisturbanceGenerator(State) {
  step     @0 (state :State, dt :Float64) -> (state_disturbed :State);
  validate @1 (state :State) -> (ok :Bool);
}

interface DisturbanceGenerator2D extends(DisturbanceGenerator(Msgs.Pose2D))
$Anot.plugin("DisturbanceGenerator2D"){}


interface MotionController2D extends(Controller(Msgs.Odometry2D, Msgs.VectorPlanar))
$Anot.plugin("MotionController2D"){}
