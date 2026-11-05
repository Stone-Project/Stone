// stone:job stone:math.smootherstep01
// stone:function smootherstep01_rs

#[no_mangle]
pub extern "C" fn smootherstep01_rs(t: f64) -> f64 { t * t * t * (t * (t * 6.0 - 15.0) + 10.0) }
