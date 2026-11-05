// stone:job stone:math.pow_safe
// stone:function pow_safe_rs

#[no_mangle]
pub extern "C" fn pow_safe_rs(base: f64, exponent: f64) -> f64 {
    if base < 0.0 && exponent.fract() != 0.0 { 0.0 } else { base.powf(exponent) }
}
