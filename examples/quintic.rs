// stone:job stone:math.quintic
// stone:function quintic_rs

#[no_mangle]
pub extern "C" fn quintic_rs(t: f64) -> f64 { t * t * t * t * t }
