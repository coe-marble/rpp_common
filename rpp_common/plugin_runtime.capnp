@0xbadbadbadbadbad5;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("rpp::runtime");

const protocolVersion :UInt32 = 1;

interface PluginRuntime {
  ping @0 ();
  shutdown @1 ();
  listAdapters @2 () -> (adapters :List(AdapterInfo));
  getComponentCapability @3 (name :Text) -> (pluginRef :Capability);
  getProtocolVersion @4 () -> (version :UInt32);
  # Names are discovery keys only. Lifecycle operations use a loaded instance's
  # immutable ID, so an unloaded/reloaded replacement cannot be controlled by
  # a stale client request.
  configureComponent @5 (instanceId :Text) -> (result :LifecycleResult);
  cleanupComponent @6 (instanceId :Text) -> (result :LifecycleResult);
  # Return every hosted slot and every registered component. Clients select a
  # connection locally, then use immutable instance IDs for lifecycle calls.
  listComponents @7 () -> (components :List(ComponentInfo));
  activateComponent @8 (instanceId :Text, state :HandoverState) -> (result :LifecycleResult);
  deactivateComponent @9 (instanceId :Text) -> (result :DeactivationResult);
  loadComponent @10 (component :ComponentServerComponent) -> (result :LifecycleResult);
  unloadComponent @11 (instanceId :Text) -> (result :LifecycleResult);
  reloadComponent @12 (instanceId :Text, transferState :Bool) -> (result :LifecycleResult);
  switchComponents @13 (
    connectionName :Text, sourceInstanceId :Text, targetInstanceId :Text,
    transferState :Bool) -> (result :LifecycleResult);
}

struct LifecycleResult {
  success @0 :Bool;
  message @1 :Text;
}

struct AdapterInfo {
  name @0 :Text;
  createdAt @1 :UInt64;
  pluginType @2 :Text;
  pluginName @3 :Text;
}

# State is type-erased only at the runtime-control boundary. Generated client
# and server adapters read/write payload using the concrete type declared by
# the lifecycle annotation. A zero schema ID and null payload mean no state.
struct HandoverState {
  schemaId @0 :UInt64;
  payload @1 :AnyPointer;
}

struct DeactivationResult {
  result @0 :LifecycleResult;
  state @1 :HandoverState;
}

struct ComponentInfo {
  name @0 :Text;
  instanceId @1 :Text;
  pluginType @2 :Text;
  pluginName @3 :Text;
  state @4 :Text;
  connectionName @5 :Text;
}

# The per-component input already accepted by component_server. The server
# owns the target slot identified by connectionName and verifies the component
# is a top-level record before it loads it.
struct ComponentServerComponent {
  componentPath @0 :Text;
  pluginName @1 :Text;
  connectionName @2 :Text;
}
