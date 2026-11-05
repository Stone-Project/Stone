// stone:job stone:math.pow
// stone:function pow_rs

#[no_mangle]
pub extern "C" fn pow_rs(x: f64, y: f64) -> f64 { x.powf(y) }
