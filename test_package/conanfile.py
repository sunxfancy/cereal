from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel = os.getenv("CONAN_CHANNEL", "ci")
username = os.getenv("CONAN_USERNAME", "sunxfancy")

class LibtestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "cereal/1.2.3@%s/%s" % (username, channel)
    generators = "cmake"
    build_policy = "missing"

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure(self, source_dir=self.conanfile_directory, build_dir="./")
        self.cmake.build(self)

    def test(self):
        self.run(os.sep.join([".","bin", "libtest"]))

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.so*", dst="bin", src="lib")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
