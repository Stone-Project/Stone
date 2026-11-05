// stone:job stone:math.wrap_degrees
// stone:function wrap_degrees_rs

#[no_mangle]
pub extern "C" fn wrap_degrees_rs(d: f64) -> f64 { (d + 180.0).rem_euclid(360.0) - 180.0 }
