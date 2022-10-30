#!lua

-- solution
solution "algo_examples"
   configurations { "Release" }

project "strat"
  kind "ConsoleApp"
  language "C++"
  includedirs {
      "../examples",
      "../",
      "/prod/algo_sdk/include",
      "/usr/local/include/decnumber",
      "/usr/local/include",
      "/usr/include",
  }
  files {
      "../examples/**.cpp",
      "../**.cpp"
  }
  objdir "../build/obj"

  configuration "Release"
      targetdir "../build/"
      defines {"NDEBUG", "USE_HDF5", "USE_QTS_LOG4","NO_PB"}
      flags {"Optimize"}
      libdirs {
          "/prod/algo_sdk/bin"
      }
      links {
          "algo_trader",
          "hiredis",
          "websockets",
          "boost_filesystem",
      }
      buildoptions {"-std=c++17", "-fPIC"}
      postbuildcommands { "rsync -avz ../build/strat ../bin" }
    
