// stone:job stone:math.half
// stone:function half_rs

#[no_mangle]
pub extern "C" fn half_rs(x: f64) -> f64 { x * 0.5 }
