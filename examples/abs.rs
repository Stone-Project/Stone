// stone:job stone:math.abs_value
// stone:function abs_rs

#[no_mangle]
pub extern "C" fn abs_rs(value: i32) -> i32 {
    if value < 0 {
        return -value;
    }
    value
}
