import sys
import json

class Localization:
    def __init__(self, language : str|None = None) -> None:
        self.language = language if language else "en"

        try:
            with open(self.__localization_file(self.language), "r", encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            print("Localization language ", self.language, " not found")
            raise e
        
    def __get_text(self, label : str) -> str:
        report = ""
        for entry in self.data[label]:
            report += entry

        return report
    
    def __getitem__(self, label : str) -> str:
        return self.__get_text(label)

    @classmethod
    def __localization_file(cls, language : str) -> str:
        folder = cls._localization_dir()
        return folder + "/" + language + ".json"
    
    @classmethod
    def _localization_dir(cls) -> str:
        file = __file__.replace('\\','/')
        dir = "/".join(file.split('/')[:-2]) + "/localization"
        return dir

# Importing localization folder
sys.path.append(Localization._localization_dir())
