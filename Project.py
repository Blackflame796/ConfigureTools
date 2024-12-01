from ConfigureProject import*
import os
import json
import sys

class Project(ConfigureProject):
    def __init__(self) -> None:
        super().__init__()
        self.filename_config = "BuildConfig.json"
        self.path_config = ""
        self.build_config = {}
        os.chdir(self.parrent_dir)
    
    def parse_presets(self) -> None:
        if os.path.exists("CMakePresets.json"):
            with open("CMakePresets.json","r+") as file:
                content = file.read()
                data = json.loads(content)

                configure_presets = data['configurePresets']
                build_presets = data['buildPresets']

                configure_preset_names = [preset['name'] for preset in configure_presets]
                build_preset_names = [preset['name'] for preset in build_presets]

                print("Configure Preset Names:")
                for name in configure_preset_names:
                    print(name)

                print("\nBuild Preset Names:")
                for name in build_preset_names:
                    print(name)

    def configure(self) -> None:
        if self.args.preset:
            configure_command = f"cmake --preset {self.args.preset}"
            os.system(configure_command)
        # toolset = ""
        # build_type = ""
        # architecture = ""
        # if sys.platform() == "win32":
        #     toolset = "MSBuild"
        # elif sys.platform() == "linux":
        #     pass
        # elif sys.platform() == "darwin":
        #     pass

        # if self.args.build_type.lower() == "debug":
        #     build_type = "Debug"
        # else:
        #     build_type = "Release"

        
        
        
    def build(self) -> None:
        build_command = "cd build && cmake --build ."
        os.system(build_command)

    def run(self) -> None:
        self.path_config = os.path.join(self.parrent_dir,self.filename_config)
        if os.path.exists(self.path_config):
            with open(self.path_config,"r+") as file: 
                content = file.read()
                self.build_config = json.loads(content)
            if os.path.exists("CMakeUserPresets.json"):
                os.remove("CMakeUserPresets.json")
                print("Delete")
            if self.build_config["writed_dependencies"] == False:
                self.write_dependencies()
            if self.build_config["configured"] == False:
                self.configure()
                self.build()
        else:
            if os.path.exists("CMakeUserPresets.json"):
                os.remove("CMakeUserPresets.json")
            self.build_config = {
                "configured":True,
                "writed_dependencies":True
            }
            self.write_dependencies()
            self.configure()
            self.build()
            with open(self.path_config,"w") as file:
                file.write(json.dumps(self.build_config))


if __name__ == "__main__":
    project = Project()
    project.get_args()
    project.parse_presets()
    project.run()