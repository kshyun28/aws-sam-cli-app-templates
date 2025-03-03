from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_python3_8_cookiecutter_aws_sam_hello_python(UnitTestBase.Python38UnitTestBase):
    directory = "python3.8/hello"
    code_directories = ["hello_world"]


class UnitTest_python3_8_cookiecutter_aws_sam_eventBridge_python(UnitTestBase.Python38UnitTestBase):
    directory = "python3.8/event-bridge"
    code_directories = ["hello_world_function"]


class UnitTest_python3_8_cookiecutter_aws_sam_eventbridge_schema_app_python(UnitTestBase.Python38UnitTestBase):
    directory = "python3.8/event-bridge-schema"
    code_directories = ["hello_world_function"]

    def _test_unit_tests(self, code_directory: str):
        self.skipTest("eventbridge schema app requires credential to pull missing files, skip")
        pass


class UnitTest_python3_8_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.Python38UnitTestBase):
    directory = "python3.8/step-func"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]


class UnitTest_python3_8_cookiecutter_aws_sam_efs_python(UnitTestBase.Python38UnitTestBase):
    directory = "python3.8/efs"
    code_directories = ["hello_efs"]


class UnitTest_python3_8_cookiecutter_aws_sam_quick_start_web_with_connectors(UnitTestBase.Python39UnitTestBase):
    directory = "python3.8/web-conn"
    code_directories = [
        "src/handlers/get_all_items", 
        "src/handlers/get_by_id", 
        "src/handlers/put_item"
    ]


class UnitTest_python3_8_cookiecutter_aws_sam_step_functions_with_connectors(UnitTestBase.Python39UnitTestBase):
    directory = "python3.8/step-func-conn"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]