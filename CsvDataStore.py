from typing import Union, Optional
from MyLogger2 import MyLogger
from pathlib import Path
from enum import Enum
import csv


class DataType(Enum):
    BOOLEAN = 0
    INTEGER = 1
    STRING = 2


class InternalData:
    def __init__(self, data_type: DataType, raw_data: Union[int, str]):
        self.data_type = data_type
        self.raw_data = raw_data


class CsvDataStore:
    log = MyLogger("CsvDataStore")
    TRUE_NUMBER = 1
    FALSE_NUMBER = 0
    DATA_NAME_INDEX = 0
    DATA_TYPE_INDEX = 1
    RAW_DATA_INDEX = 2

    def __init__(self, dir_path: Path, file_name: str):
        self.dirPath = dir_path
        self.fileName = file_name + ".csv"
        self.path = Path(self.dirPath, self.fileName)
        self.data_dict: dict[str, InternalData] = {}
        self.__read()

    def setBool(self, data_name: str, raw_data: bool) -> None:
        self.__setData(data_name, DataType.BOOLEAN, raw_data)

    def setInt(self, data_name: str, raw_data: int) -> None:
        self.__setData(data_name, DataType.INTEGER, raw_data)

    def setStr(self, data_name: str, raw_data: str) -> None:
        self.__setData(data_name, DataType.STRING, raw_data)

    def __setData(self, data_name: str, data_type: DataType, raw_data: Union[bool, int, str]) -> None:
        self.data_dict[data_name] = InternalData(data_type, raw_data)

    def getBool(self, data_name: str) -> Optional[bool]:
        return bool(self.__getData(data_name, DataType.BOOLEAN))

    def getInt(self, data_name: str) -> Optional[int]:
        value = str(self.__getData(data_name, DataType.INTEGER))
        if value.isdecimal():
            return int(value)
        return None

    def getStr(self, data_name: str) -> Optional[str]:
        return str(self.__getData(data_name, DataType.STRING))

    def __getData(self, data_name: str, data_type: DataType) -> Union[bool, int, str, None]:
        self.log.debug(self.data_dict.keys())
        if data_name not in self.data_dict.keys():
            self.log.debug("{} is not found".format(data_name))
            return None
        internalData = self.data_dict[data_name]
        if data_type == internalData.data_type == DataType.BOOLEAN:
            return bool(internalData.raw_data == self.TRUE_NUMBER)
        elif data_type == internalData.data_type == DataType.INTEGER:
            return int(internalData.raw_data)
        elif data_type == internalData.data_type == DataType.STRING:
            return str(internalData.raw_data)
        return None

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            for dataName, internalData in self.data_dict.items():
                writer.writerow([dataName, internalData.data_type.value, internalData.raw_data])

    def __read(self) -> None:
        if self.path.exists():
            with open(self.path, "r", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                for row in reader:
                    dataType = DataType(int(row[self.DATA_TYPE_INDEX]))
                    self.log.debug(row[self.DATA_NAME_INDEX])
                    self.data_dict[row[self.DATA_NAME_INDEX]] = InternalData(dataType, row[self.RAW_DATA_INDEX])


if __name__ == "__main__":
    pass
