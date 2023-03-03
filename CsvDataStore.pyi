import DataType
from pathlib import Path
from typing import Optional, Union, Dict


class CsvDataStore:
    TRUE_NUMBER: int
    FALSE_NUMBER: int
    DATA_NAME_INDEX: int
    DATA_TYPE_INDEX: int
    RAW_DATA_INDEX: int
    dirPath: Path
    fileName: str
    path: Path
    data_dict: Dict[str, Union]

    def __init__(self, dir_path: Path, file_name: str) -> None: ...

    def setBool(self, data_name: str, raw_data: bool) -> None: ...

    def setInt(self, data_name: str, raw_data: int) -> None: ...

    def setStr(self, data_name: str, raw_data: str) -> None: ...

    def getBool(self, data_name: str) -> Optional[bool]: ...

    def getInt(self, data_name: str) -> Optional[int]: ...

    def getStr(self, data_name: str) -> Optional[str]: ...

    def save(self) -> None: ...

    def __read(self) -> None: ...

    def __getData(self, data_name, param) -> Union[bool, int, str, None]: ...

    def __setData(self, data_name, param, raw_data) -> None: ...

    class InternalData:
        data_type: DataType
        raw_data: Union[int, str]

        def __init__(self, data_type: DataType, raw_data: Union[int, str]) -> None: ...
