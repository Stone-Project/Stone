// stone:job stone:math.max2
// stone:function max2_rs

#[no_mangle]
pub extern "C" fn max2_rs(x: f64, y: f64) -> f64 { if x >= y { x } else { y } }
