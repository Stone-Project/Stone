// stone:job stone:math.clamp11
// stone:function clamp11_rs

#[no_mangle]
pub extern "C" fn clamp11_rs(x: f64) -> f64 {
    if x < -1.0 { -1.0 } else if x > 1.0 { 1.0 } else { x }
}
