from configparser import ConfigParser

class Config:
    def __init__(self,file_path="src/langgraphagenticaiui/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(file_path)
    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS")
    
    def get_model_options(self):
        return self.config["DEFAULT"].get("MODEL_OPTIONS").split(",")

    def get_usecase(self):
        return self.config["DEFAULT"].get("USE_CASES")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")