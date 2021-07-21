import sys
import json

class Localization:
    global_localization = None

    def __init__(self, language : str) -> None:
        self.language = language
        try:
            with open(self.localization_file(language), "r", encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            print("Localization language ", language, " not found")
            raise e
        
    def get_text(self, label : str) -> str:
        report = ""
        for entry in self.data[label]:
            report += entry

        return report
    
    def __getitem__(self, label : str) -> str:
        return self.get_text(label)

    @classmethod
    def get(cls):
        if cls.global_localization is not None:
            return cls.global_localization
        else:
            cls.global_localization = Localization("en")
            return cls.global_localization
    
    @classmethod
    def set(cls, language):
        cls.global_localization = Localization(language)

    @classmethod
    def localization_file(cls, language : str) -> str:
        folder = cls.localization_folder()
        return folder + "/" + language + ".json"
    
    @classmethod
    def localization_folder(cls) -> str:
        file = __file__.replace('\\','/')
        localization_folder = "/".join(file.split('/')[:-2]) + "/localization"
        return localization_folder

# Importing localization folder
sys.path.append(Localization.localization_folder())