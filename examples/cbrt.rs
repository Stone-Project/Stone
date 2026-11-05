// stone:job stone:math.cbrt
// stone:function cbrt_rs

#[no_mangle]
pub extern "C" fn cbrt_rs(x: f64) -> f64 {
    x.abs().powf(1.0 / 3.0).copysign(x)
}
