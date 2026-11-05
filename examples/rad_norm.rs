// stone:job stone:math.rad_norm
// stone:function rad_norm_rs

#[no_mangle]
pub extern "C" fn rad_norm_rs(r: f64) -> f64 { r.rem_euclid(2.0 * std::f64::consts::PI) }
