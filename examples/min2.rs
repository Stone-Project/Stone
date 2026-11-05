// stone:job stone:math.min2
// stone:function min2_rs

#[no_mangle]
pub extern "C" fn min2_rs(x: f64, y: f64) -> f64 { if x <= y { x } else { y } }
