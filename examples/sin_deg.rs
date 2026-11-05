// stone:job stone:math.sin_deg
// stone:function sin_deg_rs

#[no_mangle]
pub extern "C" fn sin_deg_rs(d: f64) -> f64 { d.to_radians().sin() }
