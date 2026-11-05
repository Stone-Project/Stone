// stone:job stone:math.positive
// stone:function positive_rs

#[no_mangle]
pub extern "C" fn positive_rs(x: f64) -> bool { x > 0.0 }
