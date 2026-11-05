// stone:job stone:math.max_value
// stone:function max_rs

#[no_mangle]
pub extern "C" fn max_rs(left: i32, right: i32) -> i32 {
    if left > right {
        return left;
    }
    right
}
