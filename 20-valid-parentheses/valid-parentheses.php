class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $pairs = [
            '(' => ')',
            '{' => '}',
            '[' => ']',
        ];
        $expect = [];
        for($i = 0; $i < strlen($s); $i++) {
            if(isset($pairs[$s[$i]])) {
                $expect[] = $pairs[$s[$i]];
            } else {
                $expected = array_pop($expect);
                if($expected !== $s[$i]) {
                    return false;
                }
            }
        }
        return count($expect) === 0;
    }
}