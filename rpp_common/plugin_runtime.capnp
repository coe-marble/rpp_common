@0xbadbadbadbadbad5;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("rpp::runtime");
interface PluginRuntime {
  ping @0 ();
  shutdown @1 ();
  listAdapters @2 () -> (adapters :List(AdapterInfo));
  getComponentCapability @3 (name :Text) -> (pluginRef :Capability);
}

struct AdapterInfo {
  name @0 :Text;
  createdAt @1 :UInt64;
  pluginType @2 :Text;
  pluginName @3 :Text;
}
