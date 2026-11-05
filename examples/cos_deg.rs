// stone:job stone:math.cos_deg
// stone:function cos_deg_rs

#[no_mangle]
pub extern "C" fn cos_deg_rs(d: f64) -> f64 { d.to_radians().cos() }
