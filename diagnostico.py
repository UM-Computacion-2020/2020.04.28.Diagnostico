class CompuTools:
    def is_sorted(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True