# Modified version of array_stack.py for Goodrich, et al. textbook
# Modified by Brian O'Neill
# Changes largely reflect removal of sample use code and different package structure
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Constructor"""
        self._data = []

    def __len__(self):
        """Return number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e) # Store the new item at the end of the list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data.pop()

