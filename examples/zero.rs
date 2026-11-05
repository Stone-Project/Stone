// stone:job stone:math.zero
// stone:function zero_rs

#[no_mangle]
pub extern "C" fn zero_rs(x: f64) -> bool { x == 0.0 }
