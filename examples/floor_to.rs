// stone:job stone:math.floor_to
// stone:function floor_to_rs

#[no_mangle]
pub extern "C" fn floor_to_rs(x: f64, step: f64) -> f64 { (x / step).floor() * step }
