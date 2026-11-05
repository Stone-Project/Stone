// stone:job stone:math.smoothstep01
// stone:function smoothstep01_rs

#[no_mangle]
pub extern "C" fn smoothstep01_rs(t: f64) -> f64 { t * t * (3.0 - 2.0 * t) }
