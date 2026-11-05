// stone:job stone:math.round
// stone:function round_rs

#[no_mangle]
pub extern "C" fn round_rs(x: f64) -> f64 { (x + 0.5).floor() }
