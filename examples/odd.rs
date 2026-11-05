// stone:job stone:math.odd
// stone:function odd_rs

#[no_mangle]
pub extern "C" fn odd_rs(x: i32) -> bool { x % 2 != 0 }
