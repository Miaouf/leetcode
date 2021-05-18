class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for file in paths:
            list_files = file.split(" ")
            root = list_files[0]
            for f in list_files[1:]:
                path, data = f.split("(")
       
                dic[data].append(root+"/"+path)

        return [l for l in dic.values() if len(l)>1]
