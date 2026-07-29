@0xbadbadbadbadbad1;
using Msgs = import "rpp_common/msgs.capnp";
using Anot = import "rpp_common/anot.capnp";

interface Controller(RefState, State, Command) {
  step     @0 (ref_state: RefState, state :State, dt :Float64) -> (command :Command);
  reset    @1 ();
}


interface MotionController2D extends(Controller(Msgs.Odometry2D, Msgs.Odometry2D, Msgs.VectorPlanar))
$Anot.plugin("MotionController2D"){}

interface MotionController3D extends(Controller(Msgs.Odometry3D, Msgs.Odometry3D, Msgs.VectorSpatial))
$Anot.plugin("MotionController3D") {}


interface TwistController2D extends(Controller(Msgs.Twist2D, Msgs.Twist2D, Msgs.VectorPlanar))
$Anot.plugin("TwistController2D"){}


interface TwistController3D extends(Controller(Msgs.Twist3D, Msgs.Twist3D, Msgs.VectorSpatial))
$Anot.plugin("TwistController3D"){}

interface PoseController2D extends(Controller(Msgs.Pose2D, Msgs.Pose2D, Msgs.Twist2D))
$Anot.plugin("PoseController2D") {}

interface PoseController3D extends(Controller(Msgs.Pose3D, Msgs.Pose3D, Msgs.Twist3D))
$Anot.plugin("PoseController3D") {}


interface Allocator(ReferenceTau, AllocatedTau) {
  allocate @0 (reference :ReferenceTau) -> (allocated :AllocatedTau);
}

interface MotionControllerAllocator2D extends(Allocator(Msgs.VectorPlanar, Msgs.Command))
$Anot.plugin("MotionControllerAllocator2D"){}

interface MotionControllerAllocator3D extends(Allocator(Msgs.VectorSpatial, Msgs.Command))
$Anot.plugin("MotionControllerAllocator3D"){}
