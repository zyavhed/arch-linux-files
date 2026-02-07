class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin = minimum possible number of '(' that are currently open
        # leftMax = maximum possible number of '(' that are currently open
        leftMin, leftMax = 0, 0

        for ch in s:
            if ch == '(':
                # '(' always increases open count
                leftMin += 1
                leftMax += 1

            elif ch == ')':
                # ')' always decreases open count
                leftMin -= 1
                leftMax -= 1

            else:  # ch == '*'
                # '*' can act as:
                #   '('  -> increase open count
                #   ')'  -> decrease open count
                #   ''   -> no change
                #
                # For minimum open count, assume '*' acts as ')'
                leftMin = max(0, leftMin - 1)

                # For maximum open count, assume '*' acts as '('
                leftMax += 1

            # If even the maximum possible '(' goes negative,
            # we have more ')' than '(' in every scenario → invalid
            if leftMax < 0:
                return False

            # Minimum open count should never be negative
            # (we can always treat some '*' as empty)
            if leftMin < 0:
                leftMin = 0

        # At the end, if minimum open count is 0,
        # we can close all '(' → valid string
        return leftMin == 0
        # or retrun not leftMin > 0