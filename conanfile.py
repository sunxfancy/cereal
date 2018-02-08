from conans import ConanFile, CMake, tools

class cerealConan(ConanFile):
    name = "cereal"
    version = "1.2.2.4"
    license = "BSD license"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build_policy = "missing"
    exports = "*"

    def package(self):
        self.copy("*", dst="include", src="cereal-1.2.2/include")
        self.copy("LICENSE", dst=".", src="cereal-1.2.2/", keep_path=False)

