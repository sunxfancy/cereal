#include <cereal/archives/json.hpp>

class Test{
public:
    int x, y, z;

private:
    friend class cereal::access;

    // This method lets cereal know which data members to serialize
    template <class Archive>
    void serialize(Archive &archive)
    {
        archive(x, y, z); // serialize things by passing them to the archive
    }
};

int main(int argc, char const *argv[])
{
    Test t;
    cereal::JSONOutputArchive output(std::cout); // stream to cout
    output(cereal::make_nvp("data", t));
    return 0;
}