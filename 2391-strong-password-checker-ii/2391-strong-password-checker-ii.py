class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if (len(password)>=8) and (set(password) & set('abcdefghijklmnopqrstuvwxyz')) and (set(password) & set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) and (set(password) & set('0123456789')) and (set("!@#$%^&*()-+") & set(password)) and all(password[i] != password[i + 1] for i in range(len(password) - 1)):
            return True
        