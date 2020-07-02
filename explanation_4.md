This task is solved by recursion since the main task -- determining if a user is in a group -- can be broken down into similar sub-tasks -- determining if the user is in any of the sub-groups.

Checking if the user is in the list of users of the current input group takes O(n) time. In the worst case we will have to do this check for all subgroups of the current group recursively. So the overall time complexity is **O(n^2)**.
