// stone:job stone:math.even
// stone:function even_rs

#[no_mangle]
pub extern "C" fn even_rs(x: i32) -> bool { x % 2 == 0 }
