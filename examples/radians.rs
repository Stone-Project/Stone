// stone:job stone:math.radians
// stone:function radians_rs

#[no_mangle]
pub extern "C" fn radians_rs(d: f64) -> f64 { d.to_radians() }
