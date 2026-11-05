// stone:job stone:math.square
// stone:function square_rs

#[no_mangle]
pub extern "C" fn square_rs(value: i32) -> i32 {
    value * value
}
