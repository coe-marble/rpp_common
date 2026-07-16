@0xbadbadbadbadbad1;
using Msgs = import "rpp_common/msgs.capnp";
using Anot = import "rpp_common/anot.capnp";

interface Controller(State, Command) {
  step     @0 (state :State, dt :Float64) -> (command :Command);
  validate @1 (state :State) -> (ok :Bool);
}


interface MotionController2D extends(Controller(Msgs.Pose2D, Msgs.VectorPlanar))
$Anot.plugin("MotionController2D"){}

interface MotionController3D extends(Controller(Msgs.Pose3D, Msgs.VectorSpatial))
$Anot.plugin("MotionController3D") {}


interface Allocator(ReferenceTau, AllocatedTau) {
  allocate @0 (reference :ReferenceTau) -> (allocated :AllocatedTau);
}

interface MotionControllerAllocator2D extends(Allocator(Msgs.VectorPlanar, Msgs.Command))
$Anot.plugin("MotionControllerAllocator2D"){}

interface MotionControllerAllocator3D extends(Allocator(Msgs.VectorSpatial, Msgs.Command))
$Anot.plugin("MotionControllerAllocator3D"){}
