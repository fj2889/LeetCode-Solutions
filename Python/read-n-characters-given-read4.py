from __future__ import print_function
# Time:  O(n)
# Space: O(1)

def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        buffer = [''] * 4
        for i in xrange(n / 4 + 1):
            size = read4(buffer)
            if size:
                size = min(size, n-read_bytes)
                buf[read_bytes:read_bytes+size] = buffer[:size]
                read_bytes += size
            else:
                break
        return read_bytes

if __name__ == "__main__":
    global file_content
    buf = ['' for _ in xrange(100)]
    file_content = "a"
    print(buf[:Solution().read(buf, 9)])
    file_content = "abcdefghijklmnop"
    print(buf[:Solution().read(buf, 9)])

